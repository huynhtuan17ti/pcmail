<template>
  <div class="q-pa-md row">
    <div v-for="(name, id) in extensions" :key="id">
      <control-card
        :image="extensionImages[name]"
        :title="message_title[name]"
        @click="
          cardClicking = true;
          controller = name;
        "
      ></control-card>
    </div>

    <q-dialog v-model="cardClicking">
      <dialog-card
        :title="message_title[controller]"
        :message="message[controller]"
        :sending_format="sending_format[controller]"
      />
    </q-dialog>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { message_title, message, sending_format } from 'src/constants/gmail';

import { extensions, extensionImages } from 'src/constants/extenstions.ts';
import ControlCard from 'src/components/ControlCard.vue';
import DialogCard from 'src/components/DialogCard.vue';
import { useGapi } from 'vue-gapi';

export default defineComponent({
  name: 'HomePage',
  components: { ControlCard, DialogCard },
  setup() {
    const controller = ref('');

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
      sending_format,
      extensionImages,
      extensions,

      controller,
      cardClicking: ref(false),
    };
  },
});
</script>

<style scoped></style>
