import Vue from 'vue'
import Router from 'vue-router'
import home from '../components/home.vue'
import welcome from '../components/welcome.vue'
import about from '../components/about.vue'
Vue.use(Router)

const router = new Router({
	routes: [{
			path: '/',
			redirect: '/home'
		},
		{
			path: '/home',
			component: home,
			redirect: '/welcome',
			children: [{
					path: '/welcome',
					component: welcome
				},
				{
					path: '/about',
					component: about
				},
			]
		},
	]
})

// router.beforeEach((to, from, next) => {
// 	if (to.path === '/') {
// 		return next()
// 	}
// 	if (to.path === '/login') {
// 		return next()
// 	}
// 	if (to.path === '/userLogin') {
// 		return next()
// 	}
// 	const tokenstr = window.sessionStorage.getItem('token')
// 	if (!tokenstr) {
// 		return next('/userlogin')
// 	}
// 	next()
// })

export default router