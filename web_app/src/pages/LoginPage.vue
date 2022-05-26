<template>
  <div class="row" style="height: 100vh">
    <div class="col">
      <span class="logo-circle">
        <q-img class="logo" :src="logo"></q-img>
      </span>
    </div>
    <div class="col">
      <q-img class="login-image" :src="smartpc"></q-img>
      <div class="slogan">Control your PC with gmail</div>
      <q-btn rounded outline color="red" class="login-btn" @click="onLogin()">
        <img class="q-mr-md" :src="googleicon" style="width: 20px" />
        Login with Google
      </q-btn>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';
import logo from 'assets/logo.png';
import smartpc from 'assets/smart-pc.jpg';
import googleicon from 'assets/google-icon.png';
import { useUserStore } from 'src/stores/user';

export default defineComponent({
  setup() {
    const router = useRouter();
    const store = useUserStore();
    console.log(store);
    return {
      logo,
      smartpc,
      googleicon,
      onLogin() {
        this.$gAuth
          .signIn()
          .then((googleUser) => {
            store.onLogin();
            console.log('googleUser', googleUser);
            void router.push({ path: '/home' });
          })
          .catch((error) => {
            console.log('login error', error);
          });
      },
    };
  },
});
</script>

<style scoped lang="scss">
.logo-circle {
  display: block;
  margin: auto;
  height: 60vmin;
  width: 60vmin;
  margin-top: 15vh;
  background-color: white;
  border: 5px solid #2a4f96;
  border-radius: 50%;
  .logo {
    display: block;
    margin: auto;
    margin-top: 4vh;
    width: 50vmin;
    transition: transform 0.5s;
  }
}

.logo-circle:hover {
  border: 8px solid #255262;
  .logo {
    transform: scale(1.2);
  }
}

.login-image {
  display: block;
  margin: auto;
  margin-top: 20px;
  width: 80vmin;
}
.slogan {
  text-align: center;
  color: #2a4f96;
  font-weight: bold;
  font-size: 30px;
}
.login-btn {
  width: 20vw;
  position: relative;
  margin-top: 30px;
  left: 30%;
}
</style>
