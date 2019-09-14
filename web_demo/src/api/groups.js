import request from '@/utils/request'

// 获取用户组列表
export function getGroupList(params) {
  return request({
    url: '/Groups/',
    method: 'get',
    params
  })
}

// 创建用户组
export function createGroup(data) {
  return request({
    url: '/Groups/',
    method: 'post',
    data
  })
}

// 修改用户组
export function updateGroup(id, data) {
  return request({
    url: '/Groups/' + id + '/',
    method: 'patch',
    data
  })
}

// 删除用户组
export function deleteGroup(id) {
  return request({
    url: '/Groups/' + id + '/',
    method: 'delete'
  })
}
