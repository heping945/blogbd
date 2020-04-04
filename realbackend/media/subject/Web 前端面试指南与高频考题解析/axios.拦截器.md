```js
//axios.interceptors
api.interceptors.request.use(config => {
  console.log(config);
  console.log(vue.$store.state.userinfo);
  // 如果登录了  api请求携带请求头
  let token = vue.$store.state.userinfo.token;
  if (token) {
    config.headers["Authorization"] = "JWT " + token;
  }
  return config;
});
```
