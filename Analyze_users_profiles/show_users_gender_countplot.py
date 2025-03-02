# استيراد مكتبه باند اس
import pandas as pd

# استيراد مكتبه الرسم
import matplotlib.pyplot as plt

# استيراد مكتبه الرسم
import seaborn as sns

from get_users_profiles import get_users_profiles

def show_users_gender_countplot():

    # استيراد مكتبات معالجة اللغة العربية لضمان عرض النصوص بشكل صحيح
    import arabic_reshaper
    from bidi.algorithm import get_display

    # جلب بيانات المستخدمين من قاعدة البيانات
    df_profile = get_users_profiles()

    # تحديد حجم المخطط
    plt.subplots(figsize=(8, 6))

    # تعيين عنوان المخطط
    plt.title("Users Gender Count")

    # إعادة تشكيل النصوص العربية لضمان عرضها بشكل صحيح
    df_profile['gender'] = df_profile['gender'].apply(lambda a: get_display(arabic_reshaper.reshape(a)))

    # إنشاء مخطط عمودي لحساب عدد المستخدمين حسب الجنس
    ax = sns.countplot(x=df_profile['gender'])

    # إضافة التسميات فوق الأعمدة لعرض الأرقام
    ax.bar_label(ax.containers[0])

    # عرض المخطط
    plt.show()

show_users_gender_countplot()