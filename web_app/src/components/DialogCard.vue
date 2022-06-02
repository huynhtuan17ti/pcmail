<template>
  <q-card style="width: 60vh">
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
      <div style="margin-top: 10px">
        {{ replyMessage }}
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { subject, end_email } from 'src/constants/gmail';
import { useGapi } from 'vue-gapi';
import { findMessage } from 'src/helpers/content';

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

    function getReplyMessage() {
      var _replyMessage = '';
      gapi.getGapiClient().then((gapi) => {
        gapi.client.gmail.users.messages
          .list({
            maxResults: 1,
            userId: 'me',
            format: 'full',
            // TODO: must have from: and to: filter
            q: 'from:huynhminhtuan6429@gmail.com subject:' + subject,
          })
          .then(function (response) {
            console.log('[#] Response:');
            var messages = response.result.messages;
            if (messages && messages.length > 0) {
              for (var i = 0; i < messages.length; i++) {
                var message = messages[i];
                console.log(message.id);
                gapi.client.gmail.users.messages
                  .get({
                    userId: 'me',
                    id: message.id,
                    format: 'full',
                  })
                  .then((mail) => {
                    _replyMessage = findMessage(mail.result.payload);
                    replyMessage.value = _replyMessage; // temporary fix
                  });
              }
            } else {
              _replyMessage = 'No data found.';
              replyMessage.value = _replyMessage; // temporary fix
            }
          });
      });
    }
    // -----------------------------------------------------------

    function onClickSendMessage() {
      sendMessage(
        {
          To: end_email,
          Subject: subject,
        },
        props.message
      );
      replyMessage.value = 'Sent! Please wait until your PC reply.';
      // delay 10s waiting for response
      setTimeout(() => {
        getReplyMessage();
      }, 5000);
    }

    return {
      replyMessage,
      onClickSendMessage,
    };
  },
});
</script>
