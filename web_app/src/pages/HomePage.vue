<template>
  <div class="q-pa-md row">
    <q-card class="card">
      <q-img :src="basic"></q-img>
      <q-card-section @click="onBasicClicking()">
        <div class="text-h6" style="text-align: center">Send basic email</div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import basic from 'assets/basic.jpg';
import { useGapi } from 'vue-gapi';

export default defineComponent({
  name: 'HomePage',
  setup() {
    const gapi = useGapi();

    // load gmail API
    gapi.getGapiClient().then((gapi) => {
      gapi.load('client', () => {
        gapi.client.load('gmail', 'v1', () => {
          console.log('Loaded Gmail');
        });
      });
    });

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

    // basic message
    function onBasicClicking() {
      sendMessage(
        {
          // TODO: change here
          To: 'minhtu250802@gmail.com',
          Subject: 'Testing pcmail',
        },
        'This is a testing message. No valuable!'
      );
    }

    return {
      basic,
      onBasicClicking,
    };
  },
});
</script>

<style scoped>
.card {
  height: 30vh;
  width: 30vh;
  border-radius: 10px;
  border: 3px solid #5271ff;
  cursor: pointer;
}
</style>
