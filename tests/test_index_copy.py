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

import textwrap

from apibase import APIBase

obj = APIBase("torch.index_copy")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(5, 3)
        t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
        index = torch.tensor([0, 4, 2])
        result = torch.index_copy(x, 0, index, t)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(2, 1, 3, 3)
        t = torch.tensor([
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]], dtype=torch.float)
        index = torch.tensor([0, 1, 2])
        result = torch.index_copy(x, 2, index, t)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(5, 3)
        t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
        index = torch.tensor([0, 1, 2])
        result = torch.index_copy(x, 0, index, t)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(2, 1, 3, 3)
        t = torch.tensor([
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]], dtype=torch.float)
        index = torch.tensor([0, 1, 2])
        result = torch.index_copy(x, 2, index, t)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(20)
        t = torch.tensor([1,3,4,5], dtype=torch.float)
        index = torch.tensor([0, 12, 2, 1])
        result = torch.index_copy(x, 0, index, t)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(20)
        t = torch.tensor([1,3,4,5], dtype=torch.float)
        index = torch.tensor([0, 12, 2, 1])
        out = torch.tensor([])
        result = torch.index_copy(x, 0, index, t, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(20)
        t = torch.tensor([1,3,4,5], dtype=torch.float)
        index = torch.tensor([0, 12, 2, 1])
        out = torch.tensor([])
        result = torch.index_copy(input=x, dim=0, index=index, source=t, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])