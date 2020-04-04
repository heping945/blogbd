<!-- 处理js未知错误键值对的感悟 -->

>在处理drf后端传来的err时，有时不知道具体键值对，有时不知道几个是否有

## 不知道什么错误 ，只知道有错误
```js
var errd = {err1:'msg1',err2:'msg2'}
let k = Object.keys(errd)       
// 获得["err1", "err2"]
let v = Object.values(errd)
// 获得["msg1", "msg2"]
```

## 具体知道key

```js
var errmsg = err.response.data.username || err.response.data.password
```
