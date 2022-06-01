<template>
  <div class="q-pa-md row">
    <control-card
      :image="ExtensionImages['list_process']"
      :title="message_title['basic']"
      :message="message['basic']"
      @click="cardClicking = true"
    ></control-card>
    <control-card
      :image="ExtensionImages['poweroff']"
      :title="message_title['basic']"
      :message="message['basic']"
      @click="cardClicking = true"
    ></control-card>

    <q-dialog v-model="cardClicking">
      <dialog-card />
    </q-dialog>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { message_title, message } from 'src/constants/gmail';
import basic from 'assets/basic.jpg';
import { ExtensionImages } from 'src/constants/extenstions.ts';
import ControlCard from 'src/components/ControlCard.vue';
import DialogCard from 'src/components/DialogCard.vue';
import { useGapi } from 'vue-gapi';

export default defineComponent({
  name: 'HomePage',
  components: { ControlCard, DialogCard },
  setup() {
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
      basic,
      message,
      message_title,
      ExtensionImages,

      cardClicking: ref(false),
    };
  },
});
</script>

<style scoped></style>
