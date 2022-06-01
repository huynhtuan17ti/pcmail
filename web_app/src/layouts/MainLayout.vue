<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-toolbar class="text-primary top-bar">
        <q-img class="logo-bar" :src="logo" />
        <q-toolbar-title class="title"> PCmail </q-toolbar-title>
        <q-btn ounded outline color="blue" class="download-btn">
          <q-icon name="download" style="margin-right: 10px; cursor: point" />
          Install for your PC
        </q-btn>
        <q-btn
          flat
          round
          dense
          icon="logout"
          style="margin-left: 20px"
          @click="onLogout()"
        />
      </q-toolbar>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';
import logo from 'assets/logo_v2.png';
import downloadicon from 'assets/download-icon.png';
import { useGapi } from 'vue-gapi';
import { useUserStore } from 'src/stores/user';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'MainLayout',
  setup() {
    const gapi = useGapi();
    const store = useUserStore();
    const router = useRouter();
    function onLogout() {
      gapi.logout().then(() => {
        store.onLogout();
        void router.push({ path: '/login' });
      });
    }
    return {
      logo,
      downloadicon,
      onLogout,
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
