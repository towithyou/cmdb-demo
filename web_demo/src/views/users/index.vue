<template>
  <div class="user-list-container">
    <div style="padding-bottom: 35px;">
      <el-col :span="8">
        <el-input placeholder="搜索" v-model="params.username" @keyup.enter.native="searchClick">
          <el-button slot="append" icon="el-icon-search" @click="searchClick"></el-button>
        </el-input>
      </el-col>
    </div>
    <el-table :data="userList" border style="width: 100%">
      <el-table-column prop="id" label="ID">
      </el-table-column>
      <el-table-column prop="username" label="姓名">
      </el-table-column>
      <el-table-column prop="email" label="邮件">
      </el-table-column>
    </el-table>

    <hr>
    <center>
      <el-pagination background layout="prev, pager, next" :total="totalNum" @current-change="handleCurrentChange">
      </el-pagination>
    </center>
  </div>
</template>

<script>
  import {
    getUserList
  } from '@/api/users'

  export default {
    data() {
      return {
        userList: [],
        totalNum: 0,
        params: {
          page: 1,
          username: ''
        }
      }
    },

    created() {
      this.fetchData()
    },

    methods: {
      fetchData() {
        getUserList(this.params).then(res => {
          console.log(res)
          this.userList = res.results
          this.totalNum = res.count
        })
      },

      handleCurrentChange(val) {
        this.params.page = val
        this.fetchData()
      },

      searchClick() {
        this.params.page = 1
        this.fetchData()
      }
    }
  }

</script>

<style>

</style>
