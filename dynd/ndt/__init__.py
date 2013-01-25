from dynd._pydynd import w_dtype as dtype, \
        make_byteswap_dtype, make_fixedbytes_dtype, make_convert_dtype, \
        make_unaligned_dtype, make_fixedstring_dtype, make_string_dtype, \
        make_pointer_dtype, make_struct_dtype, make_fixedstruct_dtype, \
        make_strided_array_dtype, make_fixedarray_dtype, \
        make_categorical_dtype, \
        factor_categorical_dtype

void = dtype('void')
bool = dtype('bool')
int8 = dtype('int8')
int16 = dtype('int16')
int32 = dtype('int32')
int64 = dtype('int64')
uint8 = dtype('uint8')
uint16 = dtype('uint16')
uint32 = dtype('uint32')
uint64 = dtype('uint64')
float32 = dtype('float32')
float64 = dtype('float64')
complex_float32 = dtype('cfloat32')
complex_float64 = dtype('cfloat64')
cfloat32 = complex_float32
cfloat64 = complex_float64
# Aliases for people comfortable with the Numpy complex namings
complex64 = cfloat32
complex128 = cfloat64

string = dtype('string')
date = dtype('date')

# Includes ctypes definitions
import dynd_ctypes as ctypes

del dtype