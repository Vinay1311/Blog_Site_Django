from rest_framework_simplejwt.tokens import RefreshToken
from helper import keys
from django.core.paginator import Paginator

#---------------------------------------- Global Functions --------------------------------------------
    
def get_tokens_for_user(user):
    """
        To get tokens by mobile number
        params mobile: mobile of user 
        result: object
    """
    refresh = RefreshToken.for_user(user)
    refresh['role'] = user.role

    return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }

def pagination(queryset, page_count, page_number=10):
    paginator = Paginator(queryset, page_count)
    page_total = int(paginator.num_pages)
    total_count = int(paginator.count)
    paginated_queryset = paginator.get_page(page_number).object_list

    return paginated_queryset, {
        keys.TOTAL_PAGES: page_total, 
        keys.TOTAL_COUNT: total_count,
        keys.PAGE_NUMBER: page_number, 
        keys.PAGE_COUNT: page_count 
    }