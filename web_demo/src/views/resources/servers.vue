<template>
  <div class="resources-servers-container">
    服务器列表
    <hr>
    <el-table :data="serverList" border style="width: 100%">
      <el-table-column prop="ip" label="管理ip">
      </el-table-column>
      <el-table-column prop="hostname" label="主机名">
      </el-table-column>
      <el-table-column prop="os" label="操作系统">
      </el-table-column>
      <el-table-column prop="last_check" label="上次检测时间">
      </el-table-column>
      <el-table-column prop="device" label="网卡" type="scope">
          <template slot-scope="scope">
            <div v-for="d in scope.row.device">
                {{ d.name }}, {{ d.mac_address }}
                <span v-for="ifnet in d.ips">
                    {{ ifnet.ip }}, {{ ifnet.netmask }}
                </span>
            </div>
          </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import {
    getServersList
  } from '@/api/servers'

  export default {
    data() {
      return {
        serverList: [],
        totalNum: 0
      }
    },

    created() {
      this.fetchData()
    },

    methods: {
      fetchData() {
        getServersList(this.params).then(res => {
          console.log(res)
          this.serverList = res.results
          this.totalNum = res.count
        })
      },

      handleCurrentChange(val) {
        this.params.page = val
        this.fetchData()
      }
    }
  }

</script>
