<template>
  <div class="q-pa-md row">
    <control-card
      :image="ExtensionImages['list_process']"
      :title="message_title['basic']"
      :message="message['basic']"
    ></control-card>
    <control-card
      :image="ExtensionImages['poweroff']"
      :title="message_title['basic']"
      :message="message['basic']"
    ></control-card>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { message_title, message } from 'src/constants/gmail';
import basic from 'assets/basic.jpg';
import { ExtensionImages } from 'src/constants/extenstions.ts';
import ControlCard from 'src/components/ControlCard.vue';

export default defineComponent({
  name: 'HomePage',
  components: { ControlCard },
  setup() {
    return {
      basic,
      message,
      message_title,
      ExtensionImages,
    };
  },
});
</script>

<style scoped></style>
