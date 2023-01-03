from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# 장고의 기존 form 사용시 default로 사용하던 'auth.Form'이 아니므로 에러가 발생함
# 새로 정의한 'accounts.User'를 생성할 수 있도록 form을 재정의
# 아래 코드: 기존 'auth.Forms 에서 사용하는 UserCreationForm의 기능을
 # 모두 (meta class 포함) 가져와서 model만 우리가 정의한 모델로 ㅏㅂ꾸어줌
 # 모든 기능을 그대로 사용 가능함
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['email', 'first_name']
        