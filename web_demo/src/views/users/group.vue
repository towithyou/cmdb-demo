<template>
  <div class="user-group-container">
    <div style="padding-bottom: 35px;">
      <el-col :span="8">
        <el-input placeholder="搜索" v-model="params.name" @keyup.enter.native="searchClick">
          <el-button slot="append" icon="el-icon-search" @click="searchClick"></el-button>
        </el-input>
      </el-col>
      <el-col :span="16" style="text-align: right">
        <el-button type="primary" @click="handleAddGroupBtn">添加用户组</el-button>
      </el-col>

    </div>
    <el-table :data="groupList" border style="width: 100%">
      <el-table-column prop="id" label="ID">
      </el-table-column>
      <el-table-column prop="name" label="用户组">
      </el-table-column>
      <el-table-column prop="users" label="成员数">
        </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="handleModifyGroupClick(scope.row)" type="warning" plain><i class="el-icon-edit"></i>修改
          </el-button>
          <el-button @click="handleDeleteGroupClick(scope.row.id)" type="danger" plain><i class="el-icon-delete"></i>删除
          </el-button>
        </template>
      </el-table-column>

    </el-table>

    <el-dialog title="添加用户组" :visible.sync="addGroupFormVisible">
      <el-form :model="addGroupForm" :rules="addGroupFormRule" ref="addGroupForm">
        <el-form-item label="活动名称" :label-width="addGroupFormLabelWidth" prop="name">
          <el-input v-model="addGroupForm.name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="handleCancel">取 消</el-button>
        <el-button type="primary" @click="handleAddGroupSubmit">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog title="修改用户组" :visible.sync="groupModifyFormVisible">
      <el-form :model="groupModifyForm" :rules="addGroupFormRule" ref="groupModifyForm">
        <el-form-item label="活动名称" :label-width="addGroupFormLabelWidth" prop="name">
          <el-input v-model="groupModifyForm.name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="groupModifyFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="handleGroupModifySubmit">确 定</el-button>
      </div>
    </el-dialog>

    <hr>
    <center>
      <el-pagination background layout="prev, pager, next, total, jumper" :total="totalNum"
        @current-change="handleCurrentChange">
      </el-pagination>
    </center>
  </div>
</template>

<script>
  import {
    getGroupList,
    createGroup,
    updateGroup,
    deleteGroup
  } from '@/api/groups'

  export default {
    data() {
      return {
        groupList: [],
        totalNum: 0,
        params: {
          page: 1,
          name: ''
        },
        addGroupFormVisible: false,
        addGroupForm: {
          name: ''
        },
        addGroupFormLabelWidth: '120px',
        addGroupFormRule: {
          name: [{
            required: true,
            message: '请输入',
            trigger: 'blur'
          }]
        },
        groupModifyFormVisible: false,
        groupModifyForm: {
          id: 0,
          name: ''
        }
      }
    },

    created() {
      this.fetchData()
    },

    methods: {
      fetchData() {
        getGroupList(this.params).then(res => {
          console.log(res)
          this.groupList = res.results
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
      },

      handleAddGroupBtn() {
        this.addGroupFormVisible = true
      },

      handleAddGroupSubmit() {
        console.log(this.addGroupForm)
        createGroup(this.addGroupForm).then(res => {
          this.$message({
            message: '创建成功',
            type: 'success'
          })
          console.log(res)
          this.addGroupFormVisible = false
          this.$refs['addGroupForm'].resetFields()
          this.fetchData()
        })
      },

      handleCancel() {
        this.addGroupFormVisible = false
        this.$refs['addGroupForm'].resetFields()
      },

      handleModifyGroupClick(data_obj) {
        console.log(data_obj, '这是ID')
        console.log(data_obj.name, data_obj.id)
        this.groupModifyForm = data_obj
        this.groupModifyFormVisible = true
        console.log(this.groupModifyForm)
      },

      handleGroupModifySubmit() {
        updateGroup(this.groupModifyForm.id, this.groupModifyForm).then(res => {
          this.$message({
            message: `修改组 ${this.groupModifyForm.id} 成功`,
            type: 'success'
          })
          console.log(res)
          this.groupModifyFormVisible = false
          this.$refs['groupModifyForm'].resetFields()
          this.fetchData()
        })
      },

      handleDeleteGroupClick(id) {
        console.log(id, '进入删除状态')
        this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          deleteGroup(id).then(res => {
            this.$message({
              message: `删除组 ${id} 成功`,
              type: 'success'
            })
            this.fetchData()
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      }
    }
  }

</script>

<style>

</style>
