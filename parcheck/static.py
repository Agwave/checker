

PATTERN_STRUCT_SET = {
    "dict", "list", "set", "str", "int", "float", "bool"
}


class PatterKey:
    STRUCT_KEY = "struct"
    ELEMENTS_KEY = "elements"
    ELEMENTS_OPTIONAL_KEY = "elements_optional"


class Message:
    PATTERN_NOT_DICT_STR_LIST = "pattern 参数必须是 dict 或 str 或 list 类型"
    STRUCT_KEY_NOT_FOUND = "pattern 参数缺少 'struct' 字段"
    ELEMENTS_KEY_NOT_FOUND = "pattern 参数缺少 'elements' 字段"
    PATTERN_VALUE_NOT_FOUND = "pattern 键对应的值 '{}' 不在可选范围"
    ELEMENTS_VALUE_TYPE_ERROR = "elements 字段对应的值类型有误"
    PATTERN_STRUCT_NOT_FOUND = "未知的模板结构"
    LIST_PATTERN_ELEMENTS_STR_LIST = "list 模板类型的参数只能是 dict 或 str"