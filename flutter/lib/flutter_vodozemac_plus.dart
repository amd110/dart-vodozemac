import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:vodozemac_plus/vodozemac_plus.dart' as vod;

Future<void> init({String wasmPath = './pkg/'}) => vod.init(
      wasmPath: wasmPath,
      libraryPath: './',
      stem: !kIsWeb && (Platform.isIOS || Platform.isMacOS)
          ? 'flutter_vodozemac_plus'
          : 'vodozemac_bindings_dart',
    );
