<template>
	<div class="layout-container">
		<el-container>
			<el-main class="main-content" :style="{ width: mainWidth + 'px', height: mainHeight + 'px' }">
				<router-view></router-view>
			</el-main>
			<el-footer class="footer-content">
				<el-menu :default-active="activeIndex" class="full-height-menu" mode="horizontal"
					@select="handleSelect">
					<el-menu-item index="1">首页</el-menu-item>
					<el-menu-item index="2">我们</a></el-menu-item>
				</el-menu>
			</el-footer>
		</el-container>
	</div>
</template>

<script>
	export default {
		name: 'home',
		data() {
			return {
				mainWidth: 0,
				mainHeight: 0,
				activeIndex: '1'
			};
		},
		created() {
			switch(this.$route.path){
				case '/welcome':
					this.activeIndex = '1'
					break;
				case '/about':
					this.activeIndex = '2'
					break;
			}
		},
		mounted() {
			this.updateLayout();
			window.addEventListener('resize', this.debouncedUpdateLayout);
		},
		beforeDestroy() {
			window.removeEventListener('resize', this.debouncedUpdateLayout);
		},
		methods: {
			debouncedUpdateLayout() {
				if (this.updateTimeout) {
					clearTimeout(this.updateTimeout);
				}
				this.updateTimeout = setTimeout(this.updateLayoutDelayed, 100);
			},
			updateLayoutDelayed() {
				this.updateLayout();
			},
			updateLayout() {
				this.mainWidth = window.innerWidth;
				this.mainHeight = window.innerHeight * 0.9;
			},
			handleSelect(key) {
				if (this.activeIndex !== key) {
					this.activeIndex = key;
					switch (key) {
						case '1':
							this.$router.push('/home')
							break
						case '2':
							this.$router.push('/about')
							break
					}
				}
			}
		}

	}
</script>

<style>
	.el-header,
	.el-footer {
		background-color: #fff;
		color: #fff;
		text-align: center;
		line-height: 66px;
		padding: 0 !important;
	}


	.el-main {
		background-color: #fff;
		color: #fff;
		text-align: center;
		line-height: 160px;
	}

	body>.el-container {
		margin-bottom: 40px;
	}

	.el-container:nth-child(5) .el-aside,
	.el-container:nth-child(6) .el-aside {
		line-height: 260px;
	}

	.el-container:nth-child(7) .el-aside {
		line-height: 320px;
	}

	.layout-container {
		display: flex;
		flex-direction: column;
		height: 100vh;
		overflow: hidden;
	}

	.footer-content {
		background-color: lightgray;
	}

	.full-height-menu {
		height: 100%;
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		/* Optional padding for spacing */
	}

	.full-height-menu .el-menu-item {
		flex-grow: 1;
		text-align: center;
	}
</style>