## action

> 使用 viewsets 对 http 方式的定制

```py
        if self.action == 'retrieve':
            return UserSerializers
        elif self.action == 'list':
            return  UserSimpleSerializers

    '''
    post:create
    get:list
    retrieve:get
    destroy:delete
    update:put
    partial_update:patch
    '''
```

## 通用注册

```py
class UserRegSerializers(serializers.ModelSerializer):
    '''
    处理用户注册  api/user/       POST
    '''
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all(), message="用户已经存在")])
    password = serializers.CharField(style={'input_type': 'password'}, help_text="密码", label="密码",
                                     write_only=True, min_length=6, max_length=24)

    class Meta:
        model = UserProfile
        fields = ('username', 'password',)

    def validate_password(self, password):
        if password == '11111111':
            raise serializers.ValidationError('密码不能为11111111')
        return password

    def validate_username(self, username):
        if username == 'curry':
            raise serializers.ValidationError('不能是库里')
        elif username == 'james':
            raise serializers.ValidationError('不能是猩猩')
        return username

    # 重写 create 方法
    def create(self, validated_data):
        user = UserProfile(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    ## 对所有属性的验证和舍弃
    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs
```
