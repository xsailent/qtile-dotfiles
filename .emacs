;;; -*- lexical-binding: t; -*-
;; Загружаем тему при старте
(load-theme 'gruvbox-dark-medium t)
(electric-pair-mode 1)

;; Запрещаем Emacs спрашивать подтверждение и отключать тему
;; (параметр t в load-theme уже делает тему "безопасной",
;;  но эта строка защитит от случайного сброса)
(setq custom-enabled-themes '(gruvbox-dark-medium))

;; включить C-c C-v
(cua-mode 1)

;; C-s — сохранить файл
;; (global-set-key (kbd "C-s") 'save-buffer)

;; C-q — выйти из Emacs
;; (global-set-key (kbd "C-q") 'save-buffers-kill-terminal)

;; Поиск вперёд на M-s
;; (global-set-key (kbd "M-s") 'isearch-forward)

;; (global-set-key (kbd "M-g") 'goto-line)

;; Run compile command
(global-set-key (kbd "C-c C-c") 'compile)

;; Закрыть текущее окно (не фрейм) по C-x C-q
(global-set-key (kbd "C-x C-q") 'delete-window)

;; Открыть директорию (Dired) по C-x C-a
;; Вариант 1: Просто запрос директории
;; (global-set-key (kbd "C-x C-a") 'dired)

;; Вариант 2: Открыть директорию текущего файла (удобнее)
(global-set-key (kbd "C-x C-a") 'dired-jump)

;; Включить нумерацию строк глобально (во всех буферах)
(global-display-line-numbers-mode 1)

;; Относительные номера строк
(setq display-line-numbers-type 'relative)

;; --- Eglot (единственный LSP-клиент) ---
(use-package eglot
  :ensure nil
  :hook ((python-mode . eglot-ensure)
         (c-mode      . eglot-ensure)
         (c++-mode    . eglot-ensure)
         (rust-mode   . eglot-ensure)
         (go-mode     . eglot-ensure)
         (zig-mode    . eglot-ensure))
  :config
  ;; Не блокировать Emacs при запуске сервера
  (setq eglot-sync-connect nil)
  ;; Отключить лог событий (меньше нагрузки)
  (setq eglot-events-buffer-config '(:size 0)))

(with-eval-after-load 'company
  (setq company-idle-delay 0.3)        ; задержка 0.3 секунды после ввода для появления подсказок
  (setq company-minimum-prefix-length 2)) ; появление после ввода 2 символов

(use-package company
  :ensure t
  :config
  ;; Настройки, имитирующие поведение VS Code: быстрое появление и чувствительность
  (setq company-idle-delay 0.2)        ; задержка всплывающего окна (секунды)
  (setq company-minimum-prefix-length 1) ; показывать подсказку после ввода 1 символа
  (setq company-tooltip-align-annotations t) ; выравнивать аннотации типов
  (global-company-mode 1))

(use-package lsp-mode
  :ensure t
  :hook ((python-mode . lsp)   ; замените на нужный вам язык, например c-mode, js-mode
         (c-mode . lsp))
  :commands lsp
  :config
  ;; Использовать company для отображения подсказок (lsp-mode по умолчанию использует capf)
  (setq lsp-completion-provider :capf))

(global-completion-preview-mode 1)

(menu-bar-mode -1)
(tool-bar-mode -1)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages '(company go-mode lsp-mode lsp-pyright lsp-ui zig-mode)))


(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(put 'scroll-left 'disabled nil)
