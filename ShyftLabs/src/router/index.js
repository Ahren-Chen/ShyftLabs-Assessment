import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../components/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      //Lazy load the home view
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      //Lazy load the students view
      path: '/students',
      name: 'students',
      // route level code-splitting
      // this generates a separate chunk (students.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/Students.vue')
    },
    { 
      //Lazy load the courses view
      path: '/courses',
      name: 'courses',
      component: () => import('../components/Courses.vue')
    }
  ]
})

export default router
