# dart-vodozemac

本项目为 [vodozemac](https://github.com/matrix-org/vodozemac) Rust 库提供 Dart 和 Flutter 绑定。vodozemac 是用于 Matrix 端到端加密（E2EE）的 Olm 和 Megolm 协议的现代实现。

## 架构设计

本项目是一个采用 `flutter_rust_bridge` (FRB) v2 的 monorepo (单体仓库) 结构：

- `rust/`: 包含 Rust 实现及 FRB 绑定代码（位于 `rust/src/bindings.rs`）。
- `dart/`: 一个纯 Dart 包（`vodozemac`），封装生成的 FRB 代码，提供符合 Dart 习惯的 API。
- `flutter/`: 一个 Flutter 插件（`flutter_vodozemac`），依赖于 `vodozemac` Dart 包。
- `scripts/`: 用于测试和 CI 的辅助脚本。

## 开发工作流

### 1. 修改 Rust 代码
FRB 的入口点是 `rust/src/bindings.rs`。对公开 API 的任何更改都应在该文件中进行。

### 2. 代码生成
修改 Rust 代码或 `flutter_rust_bridge.yaml` 后，在**项目根目录**下运行以下命令：

```bash
flutter_rust_bridge_codegen generate
```

### 3. 更新 Dart API
生成的代码位于 `dart/lib/src/generated/`。请勿手动修改这些文件。
相反，请更新 `dart/lib/src/api.dart`，使用符合规范的 Dart 类和方法来暴露新功能。

### 4. 导入排序
修改 Dart 文件后，在 `dart/` 目录下运行导入排序工具：

```bash
cd dart
dart run import_sorter:main
```

## 测试

### 原生平台 (IO) 测试
在项目根目录下运行以下脚本：

```bash
./scripts/run_io_tests.sh
```

### Web 测试
在项目根目录下运行以下脚本：

```bash
./scripts/run_web_tests.sh
```

## 规范与代码风格

- **FRB 版本**: 本项目使用 `flutter_rust_bridge` v2.11.1。
- **Dart SDK**: 要求 `>=3.3.0`。
- **命名规范**: 遵循标准的 Dart 和 Rust 命名规范。
- **文档注释**: 为 `dart/lib/src/api.dart` 中所有公开的 Dart 类和方法提供清晰的文档注释。
- **线程与内存安全**: Rust 实现中使用了 `RwLock` 和 `RustOpaqueNom`，以确保跨 FFI（外部函数接口）边界的线程安全和内存管理。
---
**沟通要求：**
在本项目中，所有回复和说明请始终使用 **中文**。