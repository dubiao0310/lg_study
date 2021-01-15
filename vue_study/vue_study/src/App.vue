<template>
  <v-app>
<!-- 
    <router-link to='/testcase'><h1>index</h1></router-link> -->
    <router-view></router-view>

     <!-- <router-link to="/testcase">Go to testcase</router-link> -->
    <!-- <v-main>
      <HelloWorld/>
    </v-main> -->
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import testcase from './components/testcase';

// const Testcase = { template: testcase }

// const routes = [
//   { path: '/testcase', component: Testcase }
// ]

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
