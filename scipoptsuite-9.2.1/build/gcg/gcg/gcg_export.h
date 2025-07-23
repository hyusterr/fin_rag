
#ifndef GCG_EXPORT_H
#define GCG_EXPORT_H

#ifdef GCG_STATIC_DEFINE
#  define GCG_EXPORT
#  define GCG_NO_EXPORT
#else
#  ifndef GCG_EXPORT
#    ifdef libgcg_EXPORTS
        /* We are building this library */
#      define GCG_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define GCG_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef GCG_NO_EXPORT
#    define GCG_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef GCG_DEPRECATED
#  define GCG_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef GCG_DEPRECATED_EXPORT
#  define GCG_DEPRECATED_EXPORT GCG_EXPORT GCG_DEPRECATED
#endif

#ifndef GCG_DEPRECATED_NO_EXPORT
#  define GCG_DEPRECATED_NO_EXPORT GCG_NO_EXPORT GCG_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef GCG_NO_DEPRECATED
#    define GCG_NO_DEPRECATED
#  endif
#endif

#endif /* GCG_EXPORT_H */
