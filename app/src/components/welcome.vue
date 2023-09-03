<template>
	<div class="bodyclass">

		<div class="centered-container">
			<div class="content">
				<div style="font-size: 20px; color: black; font-weight: bold;">
					🐳 先选一下云厂商
				</div>
			</div>
		</div>

		<div class="centered-container">
			<div class="content">
				<div style="color: black;height: 20px;">
					🐟 厂商们
				</div>
			</div>
		</div>

		<div class="centered-container">
			<div v-for="(item, index) in items1" :key="index">
				<div v-if="index !== items1.length - 1"><button
						:class="['square1', { active: selectedItem1 === item.text }]" @click="toggleActive1(item.text)">
						{{ item.emoji }}{{ item.text }}
					</button></div>
				<div v-else>
					<button
						:class="['square1-1', { active: selectedItem1 === item.text }]" @click="toggleActive1(item.text)">
						{{ item.emoji }}{{ item.text }}
					</button></div>
			</div>
		</div>

		<div class="centered-container" style="margin-top: 20px;">
			<div class="content">
				<div style="color: black;height: 20px;">
					🍵 产品类型
				</div>
			</div>
		</div>

		<div class="centered-container">
			<button v-for="(item, index) in items2" :key="index"
				:class="['square2', { active: selectedItem2 === item.text }]" @click="toggleActive2(item.text)">
				{{item.emoji}}{{ item.text }}
			</button>
		</div>

		<div class="centered-container" style="margin-top: 20px;">
			<div class="content">
				<div style="color: black;height: 20px;">
					🧊 产品名称
				</div>
			</div>
		</div>

		<div class="centered-container">
			<button v-for="(item, index) in items4" :key="index" :class="['square4', { active: item.value === 1 }]"
				@click="toggleActive4(index)">
				{{item.emoji}}{{ item.text }}
			</button>
		</div>

		<div class="centercard" style="margin-top: 20px;">
			<el-card class="cardclass" shaow='always'>
				<div class="first-div centered-content" style="font-size: 20px; color: black; font-weight: bold;">
					来看看有哪些信息吧
				</div>
				<div class="centered-container">
					<button v-for="(item, index) in items3" :key="index"
						:class="['square3', { active: item.value === 1 }]" @click="toggleActive3(index)">
						{{item.emoji}}{{ item.text }}
					</button>
				</div>
				<div class="second-div centered-content">
					<div class="centered-container2">
						<div v-for="(item, index) in items5" :key="index" :class="[
					                 { square5: '产品文档' in item },
					                 { square6: '链接' in item },
					                 { square7: '帮助视频' in item }]">
							<a v-if="'产品文档' in item || '链接' in item || '帮助视频' in item"
								:href="item['产品文档'] || item['链接'] || item['帮助视频']" style="text-decoration: none;"
								target="_blank" color>
								{{item['emoji']}} {{ item['产品名称'] }}
							</a>
						</div>
					</div>
				</div>
			</el-card>
		</div>
	</div>
</template>

<script>
	import {
		dataJson
	} from "./data.js";
	export default {
		name: 'welcome',
		created() {
			this.get_all_sheet_name()
			this.get_sheet_content(0)
			setTimeout(() => {
				this.show_result(this.selectedItem2)
			}, 500);
		},
		data() {
			return {
				dataJson,
				selectedItem1: '金山云',
				selectedItem2: '中间件',
				items1: [],
				items2: [],
				items4: [],
				items3: [{
						text: '链接',
						value: 0,
						emoji: '🍥'
					}, {
						text: '产品文档',
						value: 0,
						emoji: '🍤'
					},
					{
						text: '帮助视频',
						value: 0,
						emoji: '🍪'
					},
				],
				items5: [],
				result_list: [],
				activeIndex1: null,
				activeIndex2: null,
				activeIndex3: null,
				activeIndex4: null,

			};
		},
		methods: {
			get_all_sheet_name() {
				console.log(123)
				this.$axios.get("/get_all_sheet_name").then(res => {
					if (res.data.code !== 200) {
						this.$message.error("错误")
					} else {
						var data_list = res.data.data
						var min = 0
						var max = this.dataJson.length
						for (let i = 0; i < data_list.length; i++) {
							let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
							if (i === 0) {
								var data = {
									text: data_list[i],
									value: 1,
									emoji: this.dataJson[randomInt]
								}
							} else {
								var data = {
									text: data_list[i],
									value: 0,
									emoji: this.dataJson[randomInt]
								}
							}
							console.log(data)
							this.items1.push(data)
						}
					}

				})
			},

			show_result(text) {
				this.items4 = []
				var data_list = this.result_list[text]
				var min = 0
				var max = this.dataJson.length
				for (let i = 0; i < data_list.length; i++) {
					let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
					let data = {
						text: data_list[i]['产品名称'],
						value: 0,
						emoji: this.dataJson[randomInt],
						// content:
					}
					this.items4.push(data)
				}
			},
			get_sheet_content(i) {
				this.items2 = []
				this.result_list = []
				var FormData = require('form-data');
				var data = new FormData();
				data.append('index', i);
				this.$axios.post("/get_sheet_content", data).then(res => {
					// console.log(res)
					if (res.data.code !== 200) {
						this.$message.error("错误")
					} else {
						let data_list = res.data.data
						let keys = Object.keys(data_list)
						var min = 0
						var max = this.dataJson.length
						for (let i = 0; i < keys.length; i++) {
							let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
							if (i === 0) {
								var data = {
									text: keys[i],
									value: 1,
									emoji: this.dataJson[randomInt],
									// content:
								}
							} else {
								var data = {
									text: keys[i],
									value: 0,
									emoji: this.dataJson[randomInt],
									// content:
								}
							}

							this.items2.push(data)
						}
						this.result_list = data_list
					}
				})
			},
			show_data() {
				var items2_str = ""
				for (let i = 0; i < this.items2.length; i++) {
					if (this.items2[i].value === 1) {
						items2_str = this.items2[i].text
						break
					}
				}
				var total_data_list = this.result_list[items2_str]
				var result = [];

				var flag = 0;

				for (var i = 0; i < this.items3.length; i++) {
					if (this.items3[i].value === 1) {
						flag = 1;
						break;
					}
				}

				var result = [];
				var min = 0
				var max = this.dataJson.length
				if (flag === 0) {
					for (var j = 0; j < this.items4.length; j++) {
						if (this.items4[j].value === 1) {
							for (var k = 0; k < this.items3.length; k++) {
								for (var l = 0; l < total_data_list.length; l++) {
									if (total_data_list[l]['产品名称'] === this.items4[j].text) {
										let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
										var data = {};
										data['产品名称'] = this.items4[j].text;
										data[this.items3[k].text] = total_data_list[l][this.items3[k].text];
										data['emoji'] = this.dataJson[randomInt]
										result.push(data);
									}
								}
							}

						}
					}
				} else {
					for (var m = 0; m < this.items4.length; m++) {
						if (this.items4[m].value === 1) {
							for (var n = 0; n < this.items3.length; n++) {
								if (this.items3[n].value === 1) {
									for (var o = 0; o < total_data_list.length; o++) {
										if (total_data_list[o]['产品名称'] === this.items4[m].text) {
											let randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
											var data = {};
											data['产品名称'] = this.items4[m].text;
											data[this.items3[n].text] = total_data_list[o][this.items3[n].text];
											data['emoji'] = this.dataJson[randomInt]
											result.push(data);
										}
									}
								}
							}

						}
					}
				}
				this.items5 = result
				console.log(this.items5);
			},
			toggleActive1(text) {
				this.selectedItem1 = text;
				for (let i = 0; i < this.items1.length; i++) {
					if (this.items1[i].text === text) {
						this.items1[i].value = 1
						this.get_sheet_content(i);
					} else {
						this.items1[i].value = 0
					}
				}
			},
			toggleActive2(text) {
				this.selectedItem2 = text;
				for (let i = 0; i < this.items2.length; i++) {
					if (this.items2[i].text === text) {
						this.items2[i].value = 1
						this.show_result(text)
					} else {
						this.items2[i].value = 0
					}
				}
			},
			toggleActive3(index) {
				this.items3[index].value = 1 - this.items3[index].value;
				this.show_data()
				if (this.activeIndex3 === index) {
					this.activeIndex3 = null;
				} else {
					this.activeIndex3 = index;
				}
			},

			toggleActive4(index) {
				this.items4[index].value = 1 - this.items4[index].value;
				this.show_data()
				if (this.activeIndex4 === index) {
					this.activeIndex4 = null;
				} else {
					this.activeIndex4 = index;

				}
			}
		},

	};
</script>

<style>
	.bodyclass {
		background-color: rgb(251, 251, 251);
		height: 100%;
	}

	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		max-height: 100%;
		/* 设置内容的最大高度为父容器的高度 */
		overflow: hidden;
		/* 隐藏溢出部分 */
		/* 其他样式 */
		line-height: normal;
	}

	.cardclass {
		display: flex;
		flex-direction: column;
		width: 100%;
		height: 400px;
	}

	.content img {
		max-width: 100%;
		height: 40px;
		width: 50px;
		cursor: pointer;
	}

	.custom-row {
		height: 60px;
	}

	.centercard {
		display: flex;
		justify-content: center;
		align-items: center;

	}

	.centered-content {
		display: flex;
		justify-content: center;
		align-items: center;
		padding: 10px;
		text-align: center;
		line-height: normal;
		width: 100%;
	}

	.second-div {
		height: 90%;
	}

	.centered-container {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 35px;
		/* Add this line to center vertically */

	}

	.centered-container2 {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 35px;
		flex-wrap: wrap;
	}

	.square1 {
		width: 90px;
		height: 30px;
		background-color: #e7fcee;
		border: 1px solid #bbf7d0;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #166534;
		margin: 0 5px;
		cursor: pointer;
	}


	.square1.active {
		background-color: #2dac5c;
		color: white;
		border-color: #2dac5c;
	}

	.square1:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}
	
	.square1-1 {
		width: 90px;
		height: 30px;
		background-color: #fdfdfd;
		border: 1px solid #e7e5e4;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #292524;
		margin: 0 5px;
		cursor: pointer;
	}
	
	
	.square1-1.active {
		background-color: #57534e;
		color: white;
		border-color: #57534e;
	}
	
	.square1-1:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square2 {
		width: 110px;
		height: 30px;
		background-color: #feeded;
		border: 1px solid #fecaca;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #991b1b;
		margin: 0 5px;
		cursor: pointer;
	}

	.square2.active {
		background-color: #f15656;
		color: white;
		border-color: #f15656;
	}

	.square2:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square3 {
		width: 90px;
		height: 30px;
		background-color: #f9ebde;
		border: 1px solid #f9ebde;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #9a3412;
		margin: 0 5px;
		cursor: pointer;
	}

	.square3.active {
		background-color: #f97316;
		color: white;
		border-color: #f97316;
	}

	.square3:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square4 {
		width: 150px;
		height: 40px;
		background-color: #fff9da;
		border: 1px solid #fef08a;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #854d0e;
		margin: 0 5px;
		cursor: pointer;
	}

	.square4.active {
		background-color: #eab308;
		color: white;
		border-color: #eab308;
	}

	.square4:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square5 {
		width: 150px;
		height: 30px;
		font-size: 10px;
		background-color: #e3edfa;
		border: 1px solid #bfdbfe;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 5px;
		cursor: pointer;
	}

	.square5:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square6 {
		width: 150px;
		height: 30px;
		font-size: 10px;
		background-color: #2C3E50;
		border: 1px solid #34495E;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 5px;
		cursor: pointer;
	}

	.square6:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square7 {
		width: 180px;
		height: 30px;
		font-size: 10px;
		background-color: #fdfdfd;
		border: 1px solid #e7e5e4;
		border-radius: 5px;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 5px;
		cursor: pointer;
	}

	.square7:hover {
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3);
	}

	.square5 a {
		color: #1d4ed8;
	}

	.square6 a {
		color: #FFFFFF;
	}

	.square7 a {
		color: #292524;
		/* 设置 square7 类的链接颜色为红色 */
	}
</style>