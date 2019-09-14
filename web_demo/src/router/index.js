import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '',
    component: Layout,
    redirect: '/dashboard',
    name: '主页面',
    hidden: false,
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '主页面', icon: 'dashboard', noCache: true }
    }]
  },

  {
    path: '/users',
    component: Layout,
    // name: '用户管理1',
    meta: { title: '用户管理总', icon: 'tree' },
    children: [{
      name: '用户列表3',
      path: 'list',
      component: () => import('@/views/users/index'),
      meta: { title: '用户列表', icon: 'example' }
    },
    {
      name: '用户组',
      path: 'grouplist',
      component: () => import('@/views/users/group'),
      meta: { title: '用户组', icon: 'example' }
    }]
  },

  {
    path: '/resources',
    component: Layout,
    name: '资源管理',
    meta: { title: '资源管理', icon: 'tree' },
    children: [
      {
        name: '服务器',
        path: 'servers',
        component: () => import('@/views/resources/servers'),
        meta: { title: '服务器', icon: 'example' }
      },
      {
        name: 'idc',
        path: 'idc',
        component: () => import('@/views/resources/servers'),
        meta: { title: 'idc', icon: 'example' }
      }
    ]
  },

  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

