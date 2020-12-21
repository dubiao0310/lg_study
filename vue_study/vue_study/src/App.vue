<template>
  <v-app>
    <router-view></router-view>
    <!-- <v-main>
      <HelloWorld/>
    </v-main> -->
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
