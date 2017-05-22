from django import template


register = template.Library()

@register.filter(name='yes_no')
def yes_no(bool_value, show_str):
    if bool_value:
        return show_str.partition('/')[0]
    else:
        return show_str.partition('/')[2]


#register = template.Library()
#register.filter('yes_no', yes_no)