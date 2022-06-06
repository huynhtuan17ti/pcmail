<template>
  <q-card style="width: 700px; max-width: 700px">
    <q-toolbar>
      <q-avatar>
        <q-icon name="sports_esports" color="primary" size="2.3rem" />
      </q-avatar>
      <q-toolbar-title
        ><span class="text-weight-bold">Controller </span
        >{{ title }}</q-toolbar-title
      >
      <q-btn flat round dense icon="close" v-close-popup />
    </q-toolbar>
    <q-card-section>
      <div class="text-h6" style="text-align: center; color: blue">
        PCmail status
      </div>
      <q-separator />
      <div style="margin-top: 10px; font-size: 12pt">
        <q-icon name="task_alt" color="green" size="1.5rem" />
        {{ statusMessage }}
      </div>
      <q-input
        v-show="sending_format != undefined && !isSend"
        v-model="inputMessage"
        label="Request text"
        :placeholder="sending_format"
      />
    </q-card-section>
    <div style="text-align: center; padding: 10px">
      <q-linear-progress
        query
        color="cyan"
        size="20px"
        style="margin-bottom: 20px"
        v-show="isSend && emailLink === undefined"
      >
        <div class="text-black" style="font-size: 10pt">
          Waiting for response
        </div>
      </q-linear-progress>
      <q-btn
        color="primary"
        icon-right="outgoing_mail"
        label="Send your email"
        :disable="isSend"
        style="margin-right: 20px"
        @click="
          onClickSendMessage();
          isSend = true;
        "
      />
      <q-btn
        color="primary"
        icon-right="mark_email_unread"
        label="Watch response email"
        :disable="emailLink === undefined"
        @click="onShowEmailBtnClick"
      />
    </div>
  </q-card>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { subject, end_email } from 'src/constants/gmail';
import { INBOX_URL } from 'src/constants/gapi';
import { useGapi } from 'vue-gapi';
import {
  findMessage,
  findAttachmentId,
  findMessageId,
} from 'src/helpers/content';
import { sleep } from 'src/helpers/sleep';

export default defineComponent({
  props: {
    title: String,
    message: String,
    sending_format: String,
  },
  setup(props) {
    const gapi = useGapi();

    // -----------------------------------------------------------
    // send message here
    function sendMessage(headers_obj, message) {
      var email = '';
      for (var header in headers_obj)
        email += header += ': ' + headers_obj[header] + '\r\n';

      email += '\r\n' + message;
      //console.log(email);
      gapi.getGapiClient().then((gapi) => {
        gapi.client.gmail.users.messages
          .send({
            userId: 'me',
            resource: {
              raw: btoa(email).replace(/\+/g, '-').replace(/\//g, '_'),
            },
          })
          .execute();
      });
    }

    async function getMessageData(filter) {
      var data = undefined;
      await gapi.getGapiClient().then(async (gapi) => {
        await gapi.client.gmail.users.messages
          .list({
            maxResults: 1,
            userId: 'me',
            format: 'full',
            // TODO: must have from: and to: filter
            q: filter,
          })
          .then(async (response) => {
            //console.log('[#] Response:');
            try {
              var message = response.result.messages[0];
              //console.log(message.id);
              await gapi.client.gmail.users.messages
                .get({
                  userId: 'me',
                  id: message.id,
                  format: 'full',
                })
                .then((mail) => {
                  data = mail.result;
                  //console.log(data);
                });
            } catch (err) {}
          });
      });
      return data;
    }

    // -----------------------------------------------------------
    const emailLink = ref(undefined);
    const isSend = ref(false);
    const statusMessage = ref(
      'Please fill the request (if has) and click button below to commit this action!'
    );
    const inputMessage = ref('');

    async function onClickSendMessage() {
      sendMessage(
        {
          To: end_email,
          Subject: subject,
        },
        props.message + inputMessage.value
      );
      statusMessage.value = 'Sent! Please wait until your PC reply.';
      // delay 30s waiting for response
      var data = await sleep(
        getMessageData,
        30000,
        'from:' + end_email + ' subject:' + subject
      );
      try {
        var message = findMessage(data.payload);
        statusMessage.value = 'Last message from your PC: ' + message;

        //console.log(data.payload);

        if (findAttachmentId(data.payload) !== undefined)
          statusMessage.value =
            'Found an attachment in the reply! Please click the button below to see!';

        var messageId = findMessageId(data);

        var link = INBOX_URL + messageId;
        emailLink.value = link;
      } catch (err) {
        statusMessage.value =
          'Last message from your PC: Not found any message!';
      }
    }

    function onShowEmailBtnClick() {
      window.open(
        emailLink.value,
        '_blank' // <- This is what makes it open in a new window.
      );
    }

    return {
      statusMessage,
      inputMessage,
      onClickSendMessage,
      isSend,
      emailLink,
      onShowEmailBtnClick,
      sendMessage,
    };
  },
});
</script>
