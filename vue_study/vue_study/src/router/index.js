import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Singin from '../components/Signin.vue'
import testcase from '../components/testcase.vue'
import register from '../components/register.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
    path: '/',
    name: 'singin',
    component: Singin
  },
  {
    path: '/testcase',
    name: 'testcase',
    component: testcase
  },
  {
    path: '/register',
    name: 'register',
    component: register
  }

]

const router = new VueRouter({
  routes
})

export default router
