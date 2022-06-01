<template>
  <q-card class="card" @click="onClick()">
    <q-img class="card-image" :src="image"></q-img>
    <q-card-section>
      <div class="text-h6" style="text-align: center">
        {{ title }}
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import { defineComponent } from 'vue';
import { end_email, subject } from 'src/constants/gmail';
import { useGapi } from 'vue-gapi';

export default defineComponent({
  name: 'ControlCard',
  props: {
    image: String,
    title: String,
    message: String,
  },
  setup(props) {
    const gapi = useGapi();

    // load gmail API
    // TODO: this should be a global trigger
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

    function onClick() {
      sendMessage(
        {
          // TODO: change here
          To: end_email,
          Subject: subject,
        },
        props.message
      );
    }

    return {
      onClick,
    };
  },
});
</script>

<style scoped lang="scss">
.card {
  margin: 10px;
  height: 30vh;
  width: 30vh;
  border-radius: 10px;
  border: 3px solid #5271ff;
  cursor: pointer;
  .card-image {
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    width: 70%;
  }
}
</style>
