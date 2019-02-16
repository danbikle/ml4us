; .emacs
; This file should enhance behavior of Emacs.

; \C is ctrl-key
; \e is esc-key

; I like these, you might not.
; If not, just remove them or comment them and then stop/start Emacs.

; ctrl-x , s to start a shell or return to existing shell:
(global-set-key "\C-xs" 'shell)

; Esc-p to save:
(global-set-key "\ep" 'save-buffer)


; You will probably like these enhancements:
(add-to-list 'auto-mode-alist '("\\.haml\\'" . fundamental-mode))
(global-set-key "\C-c\C-b" 'eval-buffer)
(global-set-key "\C-c\C-k" 'kill-rectangle)
(global-set-key "\C-c\C-y" 'yank-rectangle)
(global-set-key "\C-h" 'delete-backward-char)
(global-set-key "\C-x\C-i" 'insert-kbd-macro)
(global-set-key "\C-x\C-n" 'name-last-kbd-macro)
(global-set-key "\e " 'set-mark-command)
(global-set-key "\eM" 'buffer-menu-other-window)
(global-set-key "\eR" 'rename-buffer)
(global-set-key "\e[" 'backward-paragraph)
(global-set-key "\e]" 'forward-paragraph)
(global-set-key "\e^" 'query-replace-regexp)
(global-set-key "\em" 'buffer-menu-other-window)
(put 'downcase-region 'disabled nil)
(put 'upcase-region 'disabled nil)
(setq make-backup-files nil); this gets rid of those twiddles
(global-set-key "\C-xm" 'menu-bar-open) ; terminal only
; (global-set-key "\C-xm" 'x-menu-bar-open) ; GUI
; That is enough for now.
