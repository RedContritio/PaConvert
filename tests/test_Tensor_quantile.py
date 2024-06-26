# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import textwrap

from apibase import APIBase

obj = APIBase("torch.Tensor.quantile")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(0.6)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(q=0.6)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        k = 0.6
        result = x.quantile(k)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        k = 0.6
        result = x.quantile(q=k)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(0.6, dim=None)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(0.6, dim=None, keepdim=False)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(q=0.6, dim=None, keepdim=False)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(0.6, None, False)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([0., 1., 2., 3.],dtype=torch.float64)
        result = x.quantile(q=0.6, keepdim=False, dim=None)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.0795, -1.2117,  0.9765], [ 1.1707,  0.6706,  0.4884]],dtype=torch.float64)
        result = x.quantile(0.6, dim=1, keepdim=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_11():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.0795, -1.2117,  0.9765], [ 1.1707,  0.6706,  0.4884]], dtype=torch.float64)
        result = x.quantile(q=0.6, dim=1, keepdim=False, interpolation='linear')
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_12():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.0795, -1.2117,  0.9765], [ 1.1707,  0.6706,  0.4884]], dtype=torch.float64)
        result = x.quantile(q=0.6, dim=1, keepdim=False, interpolation='lower')
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_13():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.0795, -1.2117,  0.9765], [ 1.1707,  0.6706,  0.4884]], dtype=torch.float64)
        result = x.quantile(q=0.6, dim=1, keepdim=False, interpolation='higher')
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_14():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.0795, -1.2117,  0.9765], [ 1.1707,  0.6706,  0.4884]], dtype=torch.float64)
        result = x.quantile(q=0.6, dim=1, keepdim=False, interpolation='nearest')
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_15():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[ 0.0795, -1.2117,  0.9765], [ 1.1707,  0.6706,  0.4884]], dtype=torch.float64)
        result = x.quantile(q=0.6, dim=1, keepdim=False, interpolation='midpoint')
        """
    )
    obj.run(pytorch_code, ["result"])
