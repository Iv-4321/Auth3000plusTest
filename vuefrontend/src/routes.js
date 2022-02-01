import Vue from 'vue'
import VueRouter from 'vue-router'
import Posts from './views/Posts'
import Login from './views/Login'
import Logout from './views/Logout'
import Admin from './views/Admin.vue'
import Upload from './views/Upload.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
        path: '/Admin',
        name: 'Admin',
        component: Admin,
        meta: {
            requiresLogin: true
          }
        },
        {
        path: '/',
        name: 'posts',
        component: Posts,
        },
        {
        path: '/login',
        name: 'login',
        component: Login,
        },
        {
        path: '/logout',
        name: 'logout',
        component: Logout,
        },
        {
        path: '/upload',
        name: 'upload',
        component: Upload,
        },
    ]
})