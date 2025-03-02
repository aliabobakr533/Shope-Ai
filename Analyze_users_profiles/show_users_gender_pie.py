# استيراد مكتبه باند اس
import pandas as pd

# استيراد مكتبه الرسم
import matplotlib.pyplot as plt

from get_users_profiles import get_users_profiles


def show_users_gender_pie():

    # جلب بيانات المستخدمين من قاعدة البيانات
    df_profile = get_users_profiles()

    # حساب عدد المستخدمين لكل جنس
    df_gender = df_profile[['gender', 'user_id']].groupby('gender').count()

    # استيراد مكتبات معالجة اللغة العربية لتنسيق النصوص العربية بشكل صحيح
    import arabic_reshaper
    from bidi.algorithm import get_display

    # إعادة تعيين الفهرس لسهولة التعامل مع البيانات
    df_gender = df_gender.reset_index()
    print(df_gender)  # طباعة البيانات للتحقق منها

    # إعادة تشكيل النصوص العربية لضمان عرضها بشكل صحيح
    df_gender['gender'] = df_gender['gender'].apply(lambda a: get_display(arabic_reshaper.reshape(a)))

    # رسم المخطط الدائري
    plt.pie(df_gender['user_id'], labels=df_gender['gender'], autopct='%1.1f%%')

    # إضافة عنوان للمخطط
    plt.title('Gender Pie')

    # عرض المخطط
    plt.show()


show_users_gender_pie()