from django.db import models

# Create your models here.


class PositionOri(models.Model):
    position_name = models.CharField("岗位名称", max_length=100, null=True)
    company_name = models.CharField("公司名称", max_length=100, null=True)
    company_class = models.CharField("公司性质", max_length=100, null=True)
    company_scale = models.CharField("公司规模", max_length=100, null=True)
    detail_url = models.CharField("详情链接", max_length=500, null=True)

    position_base = models.CharField("城市", max_length=100, null=True)
    position_experience = models.CharField("工作经验", max_length=100, null=True)
    position_degree = models.CharField("最低学历", max_length=100, null=True)
    position_vacancies = models.CharField("招聘人数", max_length=100, null=True)
    position_salary = models.CharField("薪资", max_length=100, null=True)
    position_update_time = models.CharField("更新时间", max_length=100, null=True)
    position_skill = models.CharField("职位技能", max_length=500, null=True)
    position_description = models.TextField("岗位描述", null=True)
    position_welfare = models.CharField("职位福利", max_length=500, null=True)
    position_location = models.CharField("工作地点", max_length=500, null=True)
