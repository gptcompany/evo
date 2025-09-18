import js from '@eslint/js'

export default [
  js.configs.recommended,
  {
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        console: 'readonly',
        process: 'readonly',
        Buffer: 'readonly',
        __dirname: 'readonly',
        __filename: 'readonly',
        global: 'readonly',
        module: 'readonly',
        require: 'readonly',
        exports: 'readonly',
      }
    },
    rules: {
      // Complexity rules for refactoring support
      complexity: ['warn', 10],
      'max-depth': ['warn', 4],
      'max-lines-per-function': ['warn', 50],
      'max-nested-callbacks': ['warn', 3],
      'max-params': ['warn', 4],

      // Additional quality rules
      'no-unused-vars': 'warn',
      'no-console': 'warn',
      'prefer-const': 'error',
      'no-var': 'error',
    },
  }
];