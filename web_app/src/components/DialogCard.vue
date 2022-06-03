<template>
  <q-card style="width: 700px; max-width: 700px">
    <q-toolbar>
      <q-avatar>
        <q-icon
          name="mail_outline"
          color="green"
          size="2rem"
          style="cursor: pointer"
          @click="onClickSendMessage()"
        />
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
        <q-icon name="send" color="blue" />
        {{ replyMessage }}
      </div>
    </q-card-section>
    <div style="text-align: center; padding: 10px">
      <q-btn
        color="primary"
        icon-right="mark_email_unread"
        label="Watch your email"
        :disable="emailLink === undefined"
        @click="onEmailBtnClick"
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
  },
  setup(props) {
    const replyMessage = ref(
      'Please click the icon mail to commit this action!'
    );
    const gapi = useGapi();

    // -----------------------------------------------------------
    // send message here
    function sendMessage(headers_obj, message) {
      var email = '';
      for (var header in headers_obj)
        email += header += ': ' + headers_obj[header] + '\r\n';

      email += '\r\n' + message;
      console.log(email);
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
          });
      });
      return data;
    }

    // get the current sending message
    // async function getIdSentMessage() {
    //   console.log('get sending message!');
    //   var sent_message = await getMessage('in:sent');
    //   return sent_message.threadId;
    // }
    // -----------------------------------------------------------
    const emailLink = ref(undefined);
    async function onClickSendMessage() {
      sendMessage(
        {
          To: end_email,
          Subject: subject,
        },
        props.message
      );
      replyMessage.value = 'Sent! Please wait until your PC reply.';
      // delay 20s waiting for response
      var data = await sleep(
        getMessageData,
        20000,
        'from:' + end_email + ' subject:' + subject
      );
      var message = findMessage(data.payload);
      replyMessage.value = message;

      console.log(data.payload);

      if (findAttachmentId(data.payload) !== undefined)
        replyMessage.value =
          'Found an attachment in the reply! Please click the email icon below to see!';

      var messageId = findMessageId(data);

      var link = INBOX_URL + messageId;
      console.log(link);
      emailLink.value = link;
    }

    function onEmailBtnClick() {
      window.open(
        emailLink.value,
        '_blank' // <- This is what makes it open in a new window.
      );
    }

    return {
      replyMessage,
      onClickSendMessage,
      emailLink,
      onEmailBtnClick,
    };
  },
});
</script>
