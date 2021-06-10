from django.db import models

# Create your models here.


class Position(models.Model):
    position_name = models.CharField("岗位名称", max_length=100)
    company_name = models.CharField("公司名称", max_length=100)
    company_class = models.CharField("公司性质", max_length=100)
    company_scale = models.CharField("公司规模", max_length=100)
    detail_url = models.URLField("详情链接")

    position_base = models.CharField("城市", max_length=100)
    position_experience = models.CharField("工作经验", max_length=100)
    position_degree = models.CharField("最低学历", max_length=100)
    position_vacancies = models.IntegerField("招聘人数")
    position_min_salary = models.CharField("最低薪资", max_length=50)
    position_max_salary = models.CharField("最高薪资", max_length=50)
    position_update_time = models.CharField("更新时间", max_length=100)
    position_description = models.TextField("岗位描述")
    position_welfare = models.CharField("职位福利", max_length=100)
    position_location = models.CharField("工作地点", max_length=100)
