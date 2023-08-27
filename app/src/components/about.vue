<template>
	<div class="bodyclass">
		<div class="center1">
			<el-card class="card">
				<div class="centerfont" style="color: red;">产品</div>
				<div v-for="(item, index) in items1" :key="index" class="text">{{item.emoji}}{{item.text}}</div>
			</el-card>
		</div>
		<div class="center">
			<el-card class="card">
				<div class="centerfont" style="color: red;">开发</div>
				<div v-for="(item, index) in items2" :key="index" class="text">{{item.emoji}}{{item.text}}</div>
			</el-card>
		</div>
		<div class="center">
			<el-card class="card">
				<div class="centerfont" style="color: red;">测试</div>
				<div v-for="(item, index) in items3" :key="index" class="text">{{item.emoji}}{{item.text}}</div>
			</el-card>
		</div>
	</div>
</template>

<script>
	import {
		dataJson
	} from "./data.js";
	export default {
		data() {
			return {
				dataJson,
				items1:[],
				items2:[],
				items3:[]
			};
		},
		created() {
			this.showData()
		},
		methods: {
			showData(){
				this.items1=[]
				this.items2=[]
				this.items3=[]
				var names1=['刘琦','阿不都外力']
				var names2=['李进','吴俊广','王秋镔','曾锡文','王硕','全宏妍']
				var names3=['刘杨','蒋雅婷']
				var min = 0
				var max = this.dataJson.length
				for(let i=0;i<names1.length;i++){
					let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
					var data = {
						text:names1[i],
						emoji:this.dataJson[randomInt]
					}
					this.items1.push(data)
				}
				for(let i=0;i<names2.length;i++){
					let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
					var data = {
						text:names2[i],
						emoji:this.dataJson[randomInt]
					}
					this.items2.push(data)
				}
				for(let i=0;i<names3.length;i++){
					let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
					var data = {
						text:names3[i],
						emoji:this.dataJson[randomInt]
					}
					this.items3.push(data)
				}
			}
		},
	}
</script>

<style>
	.card{
		width: 50%;
	}
	.bodyclass{
		background-color: rgb(251,251,251);
	}
	.text{
		height: 40px;
		margin: 15px;
		line-height: normal;
	}
	.center1{
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.center{
		display: flex;
		align-items: center;
		justify-content: center;
		margin: 10px;
	}
	.centerfont{
		display: flex;
		align-items: center;
		justify-content: center;
		height: 35px;
	}
</style>