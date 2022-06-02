<template>
  <div class="q-pa-md row">
    <div v-for="(name, id) in extensions" :key="id">
      <control-card
        :image="extensionImages[name]"
        :title="message_title[name]"
        @click="
          cardClicking = true;
          gtitle = message_title[name];
          gmessage = message[name];
        "
      ></control-card>
    </div>

    <q-dialog v-model="cardClicking">
      <dialog-card :title="gtitle" :message="gmessage" />
    </q-dialog>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { message_title, message } from 'src/constants/gmail';

import { extensions, extensionImages } from 'src/constants/extenstions.ts';
import ControlCard from 'src/components/ControlCard.vue';
import DialogCard from 'src/components/DialogCard.vue';
import { useGapi } from 'vue-gapi';

export default defineComponent({
  name: 'HomePage',
  components: { ControlCard, DialogCard },
  setup() {
    const gtitle = ref('');
    const gmessage = ref('');

    // function onCardClick(title, message){
    //   gtitle.value = title
    //   gmessage.value = message

    // }

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
    return {
      message,
      message_title,
      extensionImages,
      extensions,

      gtitle,
      gmessage,
      cardClicking: ref(false),
    };
  },
});
</script>

<style scoped></style>
