# 监视屏幕尺寸 一定尺寸渲染

       <!--小于lg992视口时渲染此组件-->
            <BackTop v-if="screenwidth<992"></BackTop>
            
## 定义尺寸

        var _screenwidth = document.body.offsetWidth;
        this.screenwidth = _screenwidth
        console.log(this.screenwidth)