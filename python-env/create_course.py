
 
from setup import get_my_env_var, MissingEnvironmentVariable


SID=None
SECRET=None

try:
    SID = get_my_env_var('CLASSIN_SID')
    SECRET=get_my_env_var('CLASSIN_SECRET')
except MissingEnvironmentVariable as exc:
    print(exc)
    exit(1)









def create_course():

        '''TEST : Create One Course Record On Classin

        Read https://docs.eeo.cn/api/zh-hans/classroom/addCourse.html for instruction on how to create a new course on ClassIn system.
        Use this API to create a course. The name should be 'Course-Testing-08'
        The API keys (SID,SECRET) are set as environment variables and have been provided to you. 
        
        You should use requests libary (already installed here).
        You can create other help functions.

        Feel free to ask for help or research on the Internet.


    ''' 

    # Start here










if __name__=='__main__':
    pass






