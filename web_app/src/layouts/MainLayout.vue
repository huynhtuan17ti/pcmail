<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-toolbar class="text-primary top-bar">
        <q-img class="logo-bar" :src="logo" />
        <q-toolbar-title class="title"> PCmail </q-toolbar-title>
        <q-btn ounded outline color="blue" class="download-btn">
          <q-icon name="download" style="margin-right: 10px" />
          Install for your PC
        </q-btn>
        <q-btn flat round dense icon="logout" style="margin-left: 20px" />
      </q-toolbar>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import logo from 'assets/logo_v2.png';
import downloadicon from 'assets/download-icon.png';

export default defineComponent({
  name: 'MainLayout',
  setup() {
    return {
      logo,
      downloadicon,
    };
  },
});
</script>

<style scoped lang="scss">
.top-bar {
  height: 80px;
  border-bottom-style: solid;
  border-bottom-color: #5271ff;
  background-color: white;
  border-width: 5px;
  .title {
    margin-left: 10px;
    font-weight: bold;
    font-size: 5ch;
  }
  .logo-bar {
    width: 70px;
  }
  .download-btn {
    width: 20vw;
    position: relative;
  }
}
</style>
