<template>
  <q-card>
    <q-toolbar>
      <q-avatar>
        <q-icon name="mail_outline" color="green" size="2rem" />
      </q-avatar>
      <q-toolbar-title
        ><span class="text-weight-bold">Email</span> is sent! Waiting for
        response</q-toolbar-title
      >
      <q-btn flat round dense icon="close" v-close-popup />
    </q-toolbar>
    <q-card-section> In developing </q-card-section>
  </q-card>
</template>

<script>
import { defineComponent } from 'vue';
import { useGapi } from 'vue-gapi';

export default defineComponent({
  setup() {
    const gapi = useGapi();
    gapi.getGapiClient().then((gapi) => {
      gapi.client.gmail.users.messages
        .list({
          maxResults: 3,
          userId: 'me',
          format: 'full',
          q: 'pcmail',
        })
        .then(function (response) {
          console.log('[###] Files:');
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
                  console.log(mail.result.snippet);
                  // var encodedBody = mail.result.payload.body.data;
                  // console.log('[+] ' + encodedBody);
                  // var encodedBody = encodedBody
                  //   .replace(/-/g, '+')
                  //   .replace(/_/g, '/')
                  //   .replace(/\s/g, '');
                  // console.log(atob(encodedBody));
                });
            }
          } else {
            console.log('No files found.');
          }
        });
    });
  },
});
</script>
