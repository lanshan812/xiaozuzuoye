import Vue from 'vue'
import App from './App.vue'
//引入路由器
import VueRouter from 'vue-router'
import router from './router/index.js'
Vue.use(VueRouter)
//引入elementui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
//导入全局样式表
import './assets/global.css'
Vue.use(ElementUI)
//导入axios
import axios from 'axios'
Vue.prototype.$axios = axios 
//配置请求根路径
axios.defaults.baseURL='http://127.0.0.1:8089'

Vue.config.productionTip = false
axios.interceptors.request.use(config=>{
	config.headers.Authorization = window.sessionStorage.getItem('token')
	return config
})
new Vue({
	router:router,
	render: h => h(App),
}).$mount('#app')
