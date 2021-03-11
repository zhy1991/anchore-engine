import pytest

retreived_files = [
    ("secrets", "/etc/passwd",
     "cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYXNoCmJpbjp4OjE6MTpiaW46L2Jpbjovc2Jpbi9ub2xvZ2luCmRhZW1vbjp4OjI6MjpkYWVtb246L3NiaW46L3NiaW4vbm9sb2dpbgphZG06eDozOjQ6YWRtOi92YXIvYWRtOi9zYmluL25vbG9naW4KbHA6eDo0Ojc6bHA6L3Zhci9zcG9vbC9scGQ6L3NiaW4vbm9sb2dpbgpzeW5jOng6NTowOnN5bmM6L3NiaW46L2Jpbi9zeW5jCnNodXRkb3duOng6NjowOnNodXRkb3duOi9zYmluOi9zYmluL3NodXRkb3duCmhhbHQ6eDo3OjA6aGFsdDovc2Jpbjovc2Jpbi9oYWx0Cm1haWw6eDo4OjEyOm1haWw6L3Zhci9tYWlsOi9zYmluL25vbG9naW4KbmV3czp4Ojk6MTM6bmV3czovdXNyL2xpYi9uZXdzOi9zYmluL25vbG9naW4KdXVjcDp4OjEwOjE0OnV1Y3A6L3Zhci9zcG9vbC91dWNwcHVibGljOi9zYmluL25vbG9naW4Kb3BlcmF0b3I6eDoxMTowOm9wZXJhdG9yOi9yb290Oi9zYmluL25vbG9naW4KbWFuOng6MTM6MTU6bWFuOi91c3IvbWFuOi9zYmluL25vbG9naW4KcG9zdG1hc3Rlcjp4OjE0OjEyOnBvc3RtYXN0ZXI6L3Zhci9tYWlsOi9zYmluL25vbG9naW4KY3Jvbjp4OjE2OjE2OmNyb246L3Zhci9zcG9vbC9jcm9uOi9zYmluL25vbG9naW4KZnRwOng6MjE6MjE6Oi92YXIvbGliL2Z0cDovc2Jpbi9ub2xvZ2luCnNzaGQ6eDoyMjoyMjpzc2hkOi9kZXYvbnVsbDovc2Jpbi9ub2xvZ2luCmF0Ong6MjU6MjU6YXQ6L3Zhci9zcG9vbC9jcm9uL2F0am9iczovc2Jpbi9ub2xvZ2luCnNxdWlkOng6MzE6MzE6U3F1aWQ6L3Zhci9jYWNoZS9zcXVpZDovc2Jpbi9ub2xvZ2luCnhmczp4OjMzOjMzOlggRm9udCBTZXJ2ZXI6L2V0Yy9YMTEvZnM6L3NiaW4vbm9sb2dpbgpnYW1lczp4OjM1OjM1OmdhbWVzOi91c3IvZ2FtZXM6L3NiaW4vbm9sb2dpbgpjeXJ1czp4Ojg1OjEyOjovdXNyL2N5cnVzOi9zYmluL25vbG9naW4KdnBvcG1haWw6eDo4OTo4OTo6L3Zhci92cG9wbWFpbDovc2Jpbi9ub2xvZ2luCm50cDp4OjEyMzoxMjM6TlRQOi92YXIvZW1wdHk6L3NiaW4vbm9sb2dpbgpzbW1zcDp4OjIwOToyMDk6c21tc3A6L3Zhci9zcG9vbC9tcXVldWU6L3NiaW4vbm9sb2dpbgpndWVzdDp4OjQwNToxMDA6Z3Vlc3Q6L2Rldi9udWxsOi9zYmluL25vbG9naW4Kbm9ib2R5Ong6NjU1MzQ6NjU1MzQ6bm9ib2R5Oi86L3NiaW4vbm9sb2dpbgo="),
    ("suids", "/etc/passwd",
     "cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYXNoCmJpbjp4OjE6MTpiaW46L2Jpbjovc2Jpbi9ub2xvZ2luCmRhZW1vbjp4OjI6MjpkYWVtb246L3NiaW46L3NiaW4vbm9sb2dpbgphZG06eDozOjQ6YWRtOi92YXIvYWRtOi9zYmluL25vbG9naW4KbHA6eDo0Ojc6bHA6L3Zhci9zcG9vbC9scGQ6L3NiaW4vbm9sb2dpbgpzeW5jOng6NTowOnN5bmM6L3NiaW46L2Jpbi9zeW5jCnNodXRkb3duOng6NjowOnNodXRkb3duOi9zYmluOi9zYmluL3NodXRkb3duCmhhbHQ6eDo3OjA6aGFsdDovc2Jpbjovc2Jpbi9oYWx0Cm1haWw6eDo4OjEyOm1haWw6L3Zhci9tYWlsOi9zYmluL25vbG9naW4KbmV3czp4Ojk6MTM6bmV3czovdXNyL2xpYi9uZXdzOi9zYmluL25vbG9naW4KdXVjcDp4OjEwOjE0OnV1Y3A6L3Zhci9zcG9vbC91dWNwcHVibGljOi9zYmluL25vbG9naW4Kb3BlcmF0b3I6eDoxMTowOm9wZXJhdG9yOi9yb290Oi9zYmluL25vbG9naW4KbWFuOng6MTM6MTU6bWFuOi91c3IvbWFuOi9zYmluL25vbG9naW4KcG9zdG1hc3Rlcjp4OjE0OjEyOnBvc3RtYXN0ZXI6L3Zhci9tYWlsOi9zYmluL25vbG9naW4KY3Jvbjp4OjE2OjE2OmNyb246L3Zhci9zcG9vbC9jcm9uOi9zYmluL25vbG9naW4KZnRwOng6MjE6MjE6Oi92YXIvbGliL2Z0cDovc2Jpbi9ub2xvZ2luCnNzaGQ6eDoyMjoyMjpzc2hkOi9kZXYvbnVsbDovc2Jpbi9ub2xvZ2luCmF0Ong6MjU6MjU6YXQ6L3Zhci9zcG9vbC9jcm9uL2F0am9iczovc2Jpbi9ub2xvZ2luCnNxdWlkOng6MzE6MzE6U3F1aWQ6L3Zhci9jYWNoZS9zcXVpZDovc2Jpbi9ub2xvZ2luCnhmczp4OjMzOjMzOlggRm9udCBTZXJ2ZXI6L2V0Yy9YMTEvZnM6L3NiaW4vbm9sb2dpbgpnYW1lczp4OjM1OjM1OmdhbWVzOi91c3IvZ2FtZXM6L3NiaW4vbm9sb2dpbgpjeXJ1czp4Ojg1OjEyOjovdXNyL2N5cnVzOi9zYmluL25vbG9naW4KdnBvcG1haWw6eDo4OTo4OTo6L3Zhci92cG9wbWFpbDovc2Jpbi9ub2xvZ2luCm50cDp4OjEyMzoxMjM6TlRQOi92YXIvZW1wdHk6L3NiaW4vbm9sb2dpbgpzbW1zcDp4OjIwOToyMDk6c21tc3A6L3Zhci9zcG9vbC9tcXVldWU6L3NiaW4vbm9sb2dpbgpndWVzdDp4OjQwNToxMDA6Z3Vlc3Q6L2Rldi9udWxsOi9zYmluL25vbG9naW4Kbm9ib2R5Ong6NjU1MzQ6NjU1MzQ6bm9ib2R5Oi86L3NiaW4vbm9sb2dpbgo="),
    ("centos8", "/etc/passwd",
     "cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApiaW46eDoxOjE6YmluOi9iaW46L3NiaW4vbm9sb2dpbgpkYWVtb246eDoyOjI6ZGFlbW9uOi9zYmluOi9zYmluL25vbG9naW4KYWRtOng6Mzo0OmFkbTovdmFyL2FkbTovc2Jpbi9ub2xvZ2luCmxwOng6NDo3OmxwOi92YXIvc3Bvb2wvbHBkOi9zYmluL25vbG9naW4Kc3luYzp4OjU6MDpzeW5jOi9zYmluOi9iaW4vc3luYwpzaHV0ZG93bjp4OjY6MDpzaHV0ZG93bjovc2Jpbjovc2Jpbi9zaHV0ZG93bgpoYWx0Ong6NzowOmhhbHQ6L3NiaW46L3NiaW4vaGFsdAptYWlsOng6ODoxMjptYWlsOi92YXIvc3Bvb2wvbWFpbDovc2Jpbi9ub2xvZ2luCm9wZXJhdG9yOng6MTE6MDpvcGVyYXRvcjovcm9vdDovc2Jpbi9ub2xvZ2luCmdhbWVzOng6MTI6MTAwOmdhbWVzOi91c3IvZ2FtZXM6L3NiaW4vbm9sb2dpbgpmdHA6eDoxNDo1MDpGVFAgVXNlcjovdmFyL2Z0cDovc2Jpbi9ub2xvZ2luCm5vYm9keTp4OjY1NTM0OjY1NTM0Oktlcm5lbCBPdmVyZmxvdyBVc2VyOi86L3NiaW4vbm9sb2dpbgpkYnVzOng6ODE6ODE6U3lzdGVtIG1lc3NhZ2UgYnVzOi86L3NiaW4vbm9sb2dpbgpzeXN0ZW1kLWNvcmVkdW1wOng6OTk5Ojk5NzpzeXN0ZW1kIENvcmUgRHVtcGVyOi86L3NiaW4vbm9sb2dpbgpzeXN0ZW1kLXJlc29sdmU6eDoxOTM6MTkzOnN5c3RlbWQgUmVzb2x2ZXI6Lzovc2Jpbi9ub2xvZ2luCg==")
]


@pytest.mark.parametrize("image, path, contents", retreived_files)
def test_retreive_files(analyzed_data, image, path, contents):
    data = analyzed_data(image)
    base = data["image"]["imagedata"]['analysis_report']["retrieve_files"]["file_content.all"]["base"]
    assert base[path] == contents
