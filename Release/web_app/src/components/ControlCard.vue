<template>
  <q-card class="card">
    <q-img class="card-image" :src="image"></q-img>
    <q-card-section>
      <div class="card-title">
        {{ title }}
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ControlCard',
  props: {
    image: String,
    title: String,
  },
});
</script>

<style scoped lang="scss">
.card {
  transition: box-shadow 0.3s border 0.3s;
  margin: 20px;
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
    width: 18vh;
  }
  .card-title {
    text-align: center;
    font-size: 2vh;
  }
}
.card:hover {
  box-shadow: 8px 8px 11px rgba(33, 33, 33, 0.2);
  border: 3px solid #5ba569;
  .card-title {
    color: #5ba569;
  }
}
</style>
