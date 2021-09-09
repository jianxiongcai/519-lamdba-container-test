import json
import ast
import dill
import base64


def print_helper(content):
    print("[INFO, print_helper] {}".format(content))


def testcase_1(student_func):
    print_helper("Hello World! ")
    # json.dumps("Hello")
    return (5, 5)


def testcase_2(student_func):
    if student_func() == 1:
        return (5, 5)
    else:
        return (0, 5)


def _serialize(obj):
    '''Dill serializes Python object into a UTF-8 string'''
    byte_serialized = dill.dumps(obj, recurse = False)
    return base64.b64encode(byte_serialized).decode("utf-8")


def _deserialize(obj):
    byte_decoded = base64.b64decode(obj)
    return dill.loads(byte_decoded)


def lambda_handler(event, context):
    # read in parameters:
    # Note: AWS has some difference between local testing and remote called
    if "body" in event:
        http_params = ast.literal_eval(event['body'])
    else:
        http_params = event

    # todo (decode student_func)
    # ==== dill encoding / decoding ====
    # decode params
    # testcase_id = http_params["testcase_id"]
    # student_func = _deserialize(http_params["answer"])

    # # call testcase function
    # result_dict = {
    #     'exec_status': "INIT",
    #     'student_score': 0,
    #     'max_score': 0,
    #     'err_msg': ""
    # }

    # if testcase_id in globals().keys():
    #     try:
    #         student_score, max_score = globals()[testcase_id](student_func)
    #         result_dict['exec_status'] = "OK"
    #         result_dict['student_score'] = student_score
    #         result_dict['max_score'] = max_score
    #     except Exception as e:
    #         # if testcase contain an error
    #         raise e
    #         result_dict['exec_status'] = "FAILED"
    #         result_dict['err_msg'] = str(e)
    # else:
    #     result_dict['exec_status'] = "FAILED"
    #     result_dict['err_msg'] = "[ERROR] Testcase Not Found! Testcase ID: {}".format(testcase_id)

    # ==== end of dill test ======

    # if testcase_id in locals().keys():
    #     try:
    #         student_score, max_score = locals()[testcase_id]("Hello world! (Default Input)")
    #         result_dict['exec_status'] = "OK"
    #         result_dict['student_score'] = student_score
    #         result_dict['max_score'] = max_score
    #     except Exception as e:
    #         # if testcase contain an error
    #         result_dict['exec_status'] = "FAILED"
    #         result_dict['err_msg'] = str(e)
    # else:
    #     result_dict['exec_status'] = "FAILED"
    #     result_dict['err_msg'] = "[ERROR] Testcase Not Found! Testcase ID: {}".format(testcase_id)

    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(result_dict)
    # }

    # some simple test here
    if http_params['test_id'] == "simple":
        return {
            'statusCode': 200,
            'body': json.dumps('Test ID: {}'.format(http_params["test_id"]))
        }
    elif http_params['test_id'] == "hello":
        return {
            'statusCode': 200,
            'body': json.dumps("Hello World from Container 519")
        }
    elif http_params['test_id'] == "sklearn":
        try:
            print("[INFO] Start import sklearn")
            import sklearn
            return {
                'statusCode': 200,
                'body': json.dumps('sklearn imported')
            }
        except Exception as e:
            return {
                'statusCode': 200,
                'body': 'sklearn import failed'
            }
    


