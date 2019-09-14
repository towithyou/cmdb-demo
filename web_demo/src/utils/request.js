import axios from 'axios'
import { Message } from 'element-ui'
import store from '../store'
import { getToken } from '@/utils/auth'
import router from '../router'
// import VueRouter from 'vue-router'

// 创建axios实例
const service = axios.create({
  baseURL: process.env.BASE_API, // api的base_url
  timeout: 15000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(config => {
  if (store.getters.token) {
    config.headers['Authorization'] = 'JWT ' + getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
  }
  return config
}, error => {
  // Do something with request error
  console.log(error) // for debug
  Promise.reject(error)
})

// respone拦截器
service.interceptors.response.use(
  response => {
    /**
    * code为非20000是抛错 可结合自己业务进行修改
    */
    // console.log('request................', response.data)
    console.log('拦截器', '+++++++++++++++')
    return response.data
  },
  error => {
    console.log(error.response, '错误返回')
    if (error.response.status === 401) {
      store.dispatch('FedLogOut').then(() => {
        router.push({ path: '/login' })
        Message({
          message: '登录超时',
          type: 'error',
          duration: 5 * 1000
        })
      })
    } else if (error.response.status === 403) {
      Message({
        message: '权限拒绝',
        type: 'error',
        duration: 5 * 1000
      })
    }
    console.log('err' + error)// for debug
    return Promise.reject(error)
  }
)

export default service
