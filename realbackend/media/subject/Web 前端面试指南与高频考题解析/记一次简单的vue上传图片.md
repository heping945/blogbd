@[toc](目录)
# 记录一次简单的图片上传

```html
      <input type="file" id="upload_ele" multiple="false" accept="image/*" @change="uploadFile()" ref="img"/>
```

```js
      uploadFile() {
        var img = this.$refs.img.files[0]
        var formdata = new FormData();
        formdata.append('img', img);
        Axios({
          url: 'http://127.0.0.1:6655/api/v1/postimg/',
          method: 'post',
          data: formdata,
          headers: {'Content-Type': 'multipart/form-data'},
        }).then(res=>{
          alert('success')
          console.log(res.data)
          this.xi = res.data.img
        }).catch(err=>{
          console.log(err.response)
        })
      }
```